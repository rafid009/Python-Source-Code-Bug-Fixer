import numpy as np 

def function(x):

	l1 = x
	j3 = 9
	x = x
	paths = []
	try:
		if j3 >= 5:
			l1 = 8-l1
			x = x/5
			j3 = 1*j3
			paths.append(1)
		else:
			l1 = 8*5
			paths.append(2)
		if x > 6:
			j3 = 7+3
			j3 = 0*j3
			paths.append(3)
		else:
			l1 = l1-3
			j3 = j3-x
			j3 = j3-7
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