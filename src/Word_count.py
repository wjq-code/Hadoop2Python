from mrjob.job import MRJob
from snakebite.client import Client

client = Client('hadoop', 9000)
for l in client.text(['/input/word.txt']):
   print (l)


# class MRWordCount(MRJob):
#
#    def mapper(self,  _, line):
#       for word in line.split():
#          yield(word, 1)
#
#    def reducer(self, word, counts):
#       yield(word, sum(counts))
#
# if __name__ == '__main__':
#    MRWordCount.run()