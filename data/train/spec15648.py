import numpy as np 

def function(x):

	j3 = x
	p6 = 5
	paths = []
	try:
		if j3 < 3:
			j3 = x-p6
			paths.append(1)
		else:
			x = 0/x
			paths.append(2)
		if x <= 8:
			x = 9-1
			j3 = x+j3
			paths.append(3)
		else:
			x = x-8
			paths.append(4)
		paths.append(5)
		assert j3 >= 0
		p6 = j3**0.5
		return p6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))