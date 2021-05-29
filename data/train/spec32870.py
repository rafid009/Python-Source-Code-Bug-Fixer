import numpy as np 

def function(x):

	b1 = x
	j6 = x
	paths = []
	try:
		if b1 < 0:
			x = j6+x
			b1 = b1*b1
			j6 = b1+j6
			paths.append(1)
		else:
			x = x*3
			paths.append(2)
		if b1 < 4:
			x = x-7
			x = x+4
			paths.append(3)
		else:
			j6 = 0*b1
			j6 = 7*2
			b1 = 1-b1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j6 = x**0.5
		return j6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))