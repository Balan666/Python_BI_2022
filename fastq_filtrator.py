def gc_share(string):  # returns CG content in one string in percent
    return round((string.count('c') + string.count('C') + string.count('g') + string.count('G')) / len(string) * 100, 1)


def av_quality_dec(string):  # returns a dec number code for an average coverage of one string
    score = 0
    for letter in string:
        score += ord(letter) - 33
    return (round(score / len(string)))

def print_func(path, info, i):
    with open(path, 'a') as f_output:
        f_output.write(info[i - 1])
        f_output.write(info[i])
        f_output.write(info[i + 1])
        f_output.write(info[i + 2])


def main(input_fastq, output_file_prefix, gc_bounds=(0, 100), length_bounds=(0, 2 ** 32), quality_threshold=0,
         save_filtered=False):
    with open(input_fastq) as file0:
        file = file0.readlines()
        for i in range(1, len(file), 4):
            string = file[i].strip()
            if (type(gc_bounds) == tuple and gc_bounds[0] <= gc_share(string) <= gc_bounds[1]) \
                    or (type(gc_bounds) == int and gc_share(string) >= gc_bounds):
                gc_bound_ok = True
            else:
                gc_bound_ok = False
            if (type(length_bounds) == tuple and length_bounds[0] <= len(string) <= length_bounds[1]) \
                    or (type(length_bounds) == int and len(string) <= length_bounds):
                length_bounds_ok = True
            else:
                length_bounds_ok = False
            if gc_bound_ok and length_bounds_ok and av_quality_dec(string) > quality_threshold:
                print_func(output_file_prefix + '\\_passed.fastq', file, i)
            elif save_filtered:
                print_func(output_file_prefix + '\\_failed.fastq', file, i)

