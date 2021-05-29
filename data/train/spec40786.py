import numpy as np 

def function(x):

	p0 = x
	j6 = 7
	paths = []
	try:
		if j6 > 9:
			j6 = j6-j6
			p0 = j6+9
			x = j6-6
			paths.append(1)
		else:
			x = x/8
			j6 = 1/p0
			p0 = j6+3
			paths.append(2)
		if j6 > 0:
			j6 = 1+j6
			x = x/7
			paths.append(3)
		else:
			x = j6-4
			j6 = j6/p0
			paths.append(4)
		paths.append(5)
		assert j6 >= 0
		j6 = j6**0.5
		return j6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))