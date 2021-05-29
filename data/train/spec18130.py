import numpy as np 

def function(x):

	p7 = x
	j6 = x
	paths = []
	try:
		if x >= 7:
			j6 = j6*x
			j6 = x+8
			paths.append(1)
		else:
			x = 3*x
			paths.append(2)
		if j6 <= 5:
			p7 = p7*4
			j6 = j6-0
			paths.append(3)
		else:
			p7 = 4-2
			x = x*j6
			paths.append(4)
		paths.append(5)
		assert p7 >= 0
		j6 = p7**0.5
		return j6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))