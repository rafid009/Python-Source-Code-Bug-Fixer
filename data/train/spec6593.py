import numpy as np 

def function(x):

	j3 = 9
	n1 = 1
	paths = []
	try:
		if n1 >= 9:
			n1 = 4-n1
			n1 = 6/n1
			paths.append(1)
		else:
			j3 = 7*9
			n1 = n1+2
			paths.append(2)
		if n1 > 2:
			j3 = j3*6
			n1 = n1+x
			paths.append(3)
		else:
			j3 = x*x
			j3 = j3/4
			paths.append(4)
		paths.append(5)
		assert n1 >= 0
		j3 = n1**0.5
		return j3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))