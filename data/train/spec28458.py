import numpy as np 

def function(x):

	j2 = 8
	p3 = x
	paths = []
	try:
		if j2 <= 3:
			p3 = p3/j2
			paths.append(1)
		else:
			x = 0+x
			p3 = x+8
			paths.append(2)
		if p3 <= 3:
			x = x+j2
			p3 = p3+7
			paths.append(3)
		else:
			x = p3*7
			j2 = 7*1
			x = x+6
			paths.append(4)
		paths.append(5)
		assert p3 >= 0
		p3 = p3**0.5
		return p3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))