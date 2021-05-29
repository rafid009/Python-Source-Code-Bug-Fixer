import numpy as np 

def function(x):

	f1 = 2
	j3 = x
	paths = []
	try:
		if x < 2:
			f1 = x*x
			f1 = j3+1
			paths.append(1)
		else:
			f1 = 7+j3
			paths.append(2)
		if f1 > 0:
			j3 = 4+j3
			paths.append(3)
		else:
			x = x*6
			paths.append(4)
		paths.append(5)
		assert j3 >= 0
		j3 = j3**0.5
		return j3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))