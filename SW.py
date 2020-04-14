from Bio import SeqIO


file = 'C:/Python/testing_align.txt'


def main(file, match, mismatch, gap):


    def create_score_matrix(rows, cols):
        score_matrix = [[0 for i in range(rows)] for j in range(cols)]

        max_score = 0
        max_pos = None
        for i in range(1, rows):
            for j in range(1, cols):
                score = calc_score(score_matrix, i, j)
                if score > max_score:
                    max_score = score
                    max_pos = (i, j)

                score_matrix[i][j] = score
        return score_matrix, max_pos


    def calc_score(matrix, x, y):

        similarity = match if seq_pair[0][x - 1] == seq_pair[1][y - 1] else mismatch

        diag_score = matrix[x - 1][y - 1] + similarity
        up_score = matrix[x - 1][y] + gap
        left_score = matrix[x][y - 1] + gap

        return max(0, diag_score, up_score, left_score)


    def traceback(score_matrix, start_pos):

        END, DIAG, UP, LEFT = range(4)
        aligned_seq1 = []
        aligned_seq2 = []
        x, y = start_pos
        move = next_move(score_matrix, x, y)
        while move != END:
            if move == DIAG:
                aligned_seq1.append(seq_pair[0][x - 1])
                aligned_seq2.append(seq_pair[1][y - 1])
                x -= 1
                y -= 1
            elif move == UP:
                aligned_seq1.append(seq_pair[0][x - 1])
                aligned_seq2.append('-')
                x -= 1
            else:
                aligned_seq1.append('-')
                aligned_seq2.append(seq_pair[1][y - 1])
                y -= 1

            move = next_move(score_matrix, x, y)

        aligned_seq1.append(seq_pair[0][x - 1])
        aligned_seq2.append(seq_pair[1][y - 1])

        return ''.join(reversed(aligned_seq1)), ''.join(reversed(aligned_seq2))


    def next_move(score_matrix, x, y):

        diag = score_matrix[x - 1][y - 1]
        up = score_matrix[x - 1][y]
        left = score_matrix[x][y - 1]

        if diag >= up and diag >= left:
            return 1 if diag != 0 else 0

        elif up > diag and up >= left:
            return 2 if up != 0 else 0

        elif left > diag and left > up:
            return 3 if left != 0 else 0


    def alignment_string(aligned_seq1, aligned_seq2):

        matches, gaps, mismatches = 0, 0, 0
        alignment_string = []
        for base1, base2 in zip(aligned_seq1, aligned_seq2):
            if base1 == base2:
                alignment_string.append('|')
                matches += 1
            elif '-' in (base1, base2):
                alignment_string.append(' ')
                gaps += 1
            else:
                alignment_string.append(':')
                mismatches += 1

        return ''.join(alignment_string), matches, gaps, mismatches


    def runer(sequences):
        rows = len(sequences[0]) + 1
        cols = len(sequences[1]) + 1

        score_matrix, start_pos = create_score_matrix(rows, cols)
        seq1_aligned, seq2_aligned = traceback(score_matrix, start_pos)
        alignment_str, idents, gaps, mismatches = alignment_string(seq1_aligned, seq2_aligned)

        return seq1_aligned, seq2_aligned, alignment_str, idents, gaps, mismatches


    record = SeqIO.parse(file, 'fasta')
    global_seq_list = [i.seq for i in record]

    seq_pair = []
    if len(global_seq_list[0]) == len(global_seq_list[1]):
        seq_pair = [i for i in global_seq_list]
        s1, s2, align, idents, gaps, mismatches = runer(seq_pair)
        print(s1)
        print(align)
        print(s2)
        print(idents, gaps, mismatches)

    else:
        best_align = []
        teg = [[global_seq_list[0], len(global_seq_list[0])], [global_seq_list[1], len(global_seq_list[1])]]
        teg.sort()
        for i in range(0, teg[1][1] - teg[0][1]):
            seq_pair = [teg[0][0], teg[1][0][i: i + teg[0][1]]]
            candidate_align = [i for i in runer(seq_pair)]
            candidate_align_score = candidate_align[3] * match - candidate_align[4] * gap - candidate_align[5] * mismatch
            if len(best_align) == 0:
                best_align = [candidate_align, candidate_align_score]
            else:
                if candidate_align_score > best_align[1]:
                    best_align = [candidate_align, candidate_align_score]

        print(best_align[0][0])
        print(best_align[0][2])
        print(best_align[0][1])
        print(best_align[0][3], best_align[0][4], best_align[0][5])

if __name__ == '__main__':
    main(file, 2, -1, -1)
