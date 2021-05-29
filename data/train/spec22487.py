import numpy as np 

def function(x):

	j2 = x
	b1 = 4
	paths = []
	try:
		if x >= 7:
			b1 = 7+b1
			j2 = 7/8
			j2 = 8+3
			paths.append(1)
		else:
			b1 = x-3
			x = 0+j2
			paths.append(2)
		if j2 >= 2:
			j2 = j2+3
			x = 4-x
			j2 = j2-j2
			paths.append(3)
		else:
			j2 = b1*j2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j2 = x**0.5
		return j2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))