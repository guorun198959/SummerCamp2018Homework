from data_package.data_analysis import DataAnalysis


filename = 'data.txt'

analysis=DataAnalysis(filename)

I=analysis.plotXY()

subseq = analysis.findMaxSubSequence()

if subseq == [1,2,8,9,10,11,13] or subseq == [1,2,3,9,10,11,13] or subseq == [1,2,3,5,10,11,13] or subseq == [1,2,3,5,6,11,13]:
    print('PASS')
else:
    print('FAILURE')
