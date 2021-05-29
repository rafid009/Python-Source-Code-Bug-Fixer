import numpy as np 

def function(x):

	j6 = x
	b1 = 5
	x = 1
	paths = []
	try:
		if j6 >= 1:
			j6 = 4*j6
			x = 0*x
			j6 = j6*9
			paths.append(1)
		else:
			b1 = x+1
			b1 = b1/9
			paths.append(2)
		if j6 > 3:
			j6 = j6+7
			paths.append(3)
		else:
			j6 = 3+j6
			paths.append(4)
		paths.append(5)
		assert j6 >= 0
		b1 = j6**0.5
		return b1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))