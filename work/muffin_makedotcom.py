# with open('/Users/alex/Documents/the_odin_project/git_test/work/x.txt', 'w') as f:
#     for i in range ( 1 , 301 ):
#         f.write(str(i) + " {{1.fields["+str(i)+"].label}}")
#         f.write('\n')
#         for j in range (1,10):
#             f.write("{{1.fields["+str(i)+"].values["+str(j)+"].answer}}")
#             f.write('\n')
#         f.write("---")
#         f.write('\n')
# print("Done")
# f.close()

with open('/Users/alex/Documents/the_odin_project/git_test/work/x.txt', 'w') as f:
    for i in range ( 1 , 234 ):
        f.write(str(i) + " {{1.fields["+str(i)+"].label}}")
        f.write('\n')
        f.write("{{1.fields["+str(i)+"].values[1].answer}}")
        f.write('\n')
        f.write("---")
        f.write('\n')
print("Done")
f.close()