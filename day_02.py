import numpy as np

reports = []

with open('data/day_02.txt') as f:
    for line in f:
        report = np.array(list(map(int, line.strip().split())))
        reports.append(report)


def check_report(r, weak=False):
    diffs = r[1:] - r[:-1]
    if diffs[0] < 0:
        diffs *= -1
    if np.all(diffs > 0) and np.all(diffs < 4):
        return True
    elif weak:
        bad_index = np.argwhere(~((diffs > 0) * (diffs < 4)))[0][0]
        new_r_before = np.delete(r, bad_index)
        new_r_after = np.delete(r, bad_index + 1)
        new_r_first = r[1:]
        return check_report(new_r_before) or check_report(new_r_after) or check_report(new_r_first)
    return False


print(sum(check_report(report) for report in reports))
print(sum(check_report(report, weak=True) for report in reports))

