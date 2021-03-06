



def calculate_cross(recall, precision):
    total = 246467
    actual_pos = 107839

    true_pos = recall * actual_pos
    false_pos = true_pos / precision - true_pos
    false_neg = actual_pos - true_pos
    true_neg = total - true_pos - false_pos - false_neg

    s = ""
    s += 'Total amount of samples & ' + str(total) + " \\\\" + "\n"
    s += 'False negative & ' + str(false_neg) + " \\\\" + "\n"
    s += 'False positive & ' + str(false_pos) + " \\\\" + "\n"
    s += 'True negative & ' + str(true_neg) + " \\\\" + "\n"
    s += 'True positive & ' + str(true_pos) + " \\\\" + "\n"
    print s

def calculate_ctu(recall, precision):
    total = 195519
    actual_pos = 708.9 + 56182.1

    true_pos = recall * actual_pos
    false_pos = true_pos / precision - true_pos
    false_neg = actual_pos - true_pos
    true_neg = total - true_pos - false_pos - false_neg

    s = ""
    s += 'Total amount of samples & ' + str(total) + " \\\\" + "\n"
    s += 'False negative & ' + str(false_neg) + " \\\\" + "\n"
    s += 'False positive & ' + str(false_pos) + " \\\\" + "\n"
    s += 'True negative & ' + str(true_neg) + " \\\\" + "\n"
    s += 'True positive & ' + str(true_pos) + " \\\\" + "\n"
    print s

def calculate_class(recall, precision):
    total = 226467
    actual_pos = 13077 + 74762

    true_pos = recall * actual_pos
    false_pos = true_pos / precision - true_pos
    false_neg = actual_pos - true_pos
    true_neg = total - true_pos - false_pos - false_neg

    s = ""
    s += 'Total amount of samples & ' + str(total) + " \\\\" + "\n"
    s += 'False negative & ' + str(false_neg) + " \\\\" + "\n"
    s += 'False positive & ' + str(false_pos) + " \\\\" + "\n"
    s += 'True negative & ' + str(true_neg) + " \\\\" + "\n"
    s += 'True positive & ' + str(true_pos) + " \\\\" + "\n"
    print s

import sys
if __name__ == "__main__":
    if len(sys.argv) == 4:
        if sys.argv[1] == "ctu":
            calculate_ctu(float(sys.argv[2]), float(sys.argv[3]))
        elif sys.argv == "cross":
            calculate_cross(float(sys.argv[2]), float(sys.argv[3]))
