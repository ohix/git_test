with open('/Users/alex/Documents/the_odin_project/git_test/work/x.txt', 'w') as f:
    for i in range ( 1 , 301 ):
        f.write(str(i) + " {{1.fields["+str(i)+"].label}}")
        f.write('\n')
        for j in range (1,1):
            f.write("{{1.fields["+str(i)+"].values["+str(j)+"].answer}}")
            f.write('\n')
        f.write("---")
        f.write('\n')
print("Done")
f.close()