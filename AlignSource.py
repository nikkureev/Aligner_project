def main_func(file, match, mismatch, gap, method):

    if method == 'local':
        match, mismatch, gap = 1, 0, 0


    def create_score_matrix(rows, cols):
        score_matrix = [[0 for i in range(cols + 1)] for j in range(rows + 1)]
        score_matrix[0] = [i for i in list(range(cols + 1))]
        j = 0
        for k in score_matrix:
            k[0] = j
            j += 1

        max_pos = None
        for i in range(1, rows):
            for j in range(1, cols):
                score = calc_score(score_matrix, i, j)
                score_matrix[i][j] = score
                max_pos = (i, j)

        return score_matrix, max_pos


    def calc_score(matrix, x, y):

        similarity = match if seq_pair[0][x - 1] == seq_pair[1][y - 1] else mismatch

        if method == 'local':
            diag_score = similarity
            up_score = gap
            left_score = gap
        else:
            diag_score = matrix[x - 1][y - 1] + similarity
            up_score = matrix[x - 1][y] + gap
            left_score = matrix[x][y - 1] + gap

        return max(0, diag_score, up_score, left_score)


    def global_traceback(score_matrix, start_pos):

        DIAG, UP, LEFT = range(3)

        aligned_seq1 = []
        aligned_seq2 = []


        x, y = start_pos
        coordinates = [[], []]
        move = next_move(score_matrix, x, y)
        while x > 0 and y > 0:
            coordinates[0].append(x)
            coordinates[1].append(y)
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

        aligned_seq1.append(seq_pair[0][x])
        aligned_seq2.append(seq_pair[1][y])

        return ''.join(reversed(aligned_seq1)), ''.join(reversed(aligned_seq2)), coordinates


    def local_traceback(score_matrix):

        score_matrix.append([0 for i in range(len(score_matrix[0]))])
        for lines in score_matrix:
            lines.append(0)

        aligned_seq1 = []
        aligned_seq2 = []

        score_matrix.append([0 for i in range(len(score_matrix[0]))])
        for lines in score_matrix:
            lines.append(0)

        diag_sum, start_list = [], []
        for i in range(len(score_matrix)):
            for j in range(len(score_matrix[i])):
                if score_matrix[i][j] == 1:
                    if [i, j] not in start_list:
                        start_list.append([i, j])
                        k = 1
                        local_diag = [[i, j]]
                        while score_matrix[i + k][j + k] != 0:
                            start_list.append([i + k, j + k])
                            local_diag.append([i + k, j + k])
                            k += 1
                        diag_sum.append(local_diag)

        longest = []
        for variants in diag_sum:
            if len(longest) < len(variants):
                longest = variants

        coordinates = [[], []]
        for i in longest:
            aligned_seq1.append(seq_pair[0][i[0] - 1])
            coordinates[0].append(i[0] - 1)
            aligned_seq2.append(seq_pair[1][i[1] - 1])
            coordinates[1].append(i[1] - 1)

        return ''.join(aligned_seq1), ''.join(aligned_seq2), coordinates



    def next_move(score_matrix, x, y):

        diag = score_matrix[x - 1][y - 1]
        up = score_matrix[x - 1][y]
        left = score_matrix[x][y - 1]

        if diag >= up and diag >= left:
            return 0

        elif up > diag and up >= left:
            return 1

        elif left > diag and left > up:
            return 2


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
        if method == 'local':
            seq1_aligned, seq2_aligned, draw_list = local_traceback(score_matrix)
        else:
            seq1_aligned, seq2_aligned, draw_list = global_traceback(score_matrix, start_pos)

        alignment_str, idents, gaps, mismatches = alignment_string(seq1_aligned, seq2_aligned)

        return seq1_aligned, seq2_aligned, alignment_str, idents, gaps, mismatches, draw_list


    def fastaParser(infile):
        seqs = []
        headers = []
        with open(infile, 'r') as f:
            sequence = ""
            header = None
            for line in f:
                if line.startswith('>'):
                    headers.append(line[1:-1])
                    if header:
                        seqs.append(sequence)
                    sequence = ""
                    header = line[1:]
                else:
                    sequence += line.rstrip()
            seqs.append(sequence)
        return headers, seqs


    parsed = fastaParser(file)
    seq_pair = [parsed[1][0], parsed[1][1]]

    s1, s2, align, idents, gaps, mismatches, for_draw = runer(seq_pair)
    return s1, s2, align, idents, gaps, mismatches, for_draw