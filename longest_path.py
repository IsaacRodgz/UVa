"""
dir
\t subdir1
\t \t file1.ext
\t \t subsubdir1
\t subdir2
\t \t subsubdir2
\t \t \t file2.ext

{0:0}

"""

def lengthLongestPath(input: str) -> int:
    all_dirs = []
    current_dir = []
    prev_depth = -1

    for line in input.split("\n"):
        if prev_depth == -1:
            current_dir.append(line)
            all_dirs.append(line)
            prev_depth += 1
        else:
            tokens = line.split("\t")
            curr_depth = len(tokens[:-1])
            if curr_depth <= prev_depth:
                diff = abs(curr_depth-prev_depth)+1
                for i in range(diff):
                    current_dir.pop()
            current_dir.append(tokens[-1])
            all_dirs.append("/".join(current_dir))
            prev_depth = curr_depth

    return max([len(s) for s in all_dirs])

print(lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"))
