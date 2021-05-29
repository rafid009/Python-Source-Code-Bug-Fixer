import numpy as np 

def function(x):

	j6 = x
	p7 = x
	x = 7
	paths = []
	try:
		if p7 < 7:
			j6 = j6+5
			p7 = 6*p7
			x = j6/x
			paths.append(1)
		else:
			j6 = 8*3
			paths.append(2)
		if x < 1:
			x = 0-j6
			j6 = j6*2
			j6 = j6+j6
			paths.append(3)
		else:
			p7 = p7*6
			paths.append(4)
		paths.append(5)
		assert p7 >= 0
		p7 = p7**0.5
		return p7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))