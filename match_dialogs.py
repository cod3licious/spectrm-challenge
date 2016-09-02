import sys



if __name__ == '__main__':
    """
    This script should be called as 
        python match_dialogs.py path/to/test_dialogs.txt path/to/test_missing.txt
    and write the predicted conversation numbers for all missing lines to a file 
    named test_missing_with_predictions.txt 
    """
    # if called with file names, load data from there else load from default location / output an error
    if len(sys.argv) > 2:
        test_dialogs_file, test_missing_file = sys.argv[1], sys.argv[2]
    else:
        print "please call this script with `python match_dialogs.py path/to/test_dialogs.txt path/to/test_missing.txt`"
