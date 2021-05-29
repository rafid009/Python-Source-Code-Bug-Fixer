import numpy as np 

def function(x):

	p7 = x
	j2 = x
	paths = []
	try:
		if j2 <= 4:
			x = x*3
			paths.append(1)
		else:
			p7 = 9+7
			paths.append(2)
		if p7 < 8:
			p7 = p7+p7
			paths.append(3)
		else:
			p7 = 7-1
			x = x/1
			p7 = 7/p7
			paths.append(4)
		paths.append(5)
		assert p7 >= 0
		j2 = p7**0.5
		return j2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))