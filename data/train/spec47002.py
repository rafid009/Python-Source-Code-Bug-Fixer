import numpy as np 

def function(x):

	p7 = 8
	u3 = 0
	paths = []
	try:
		if u3 > 9:
			p7 = 4*p7
			x = x-6
			paths.append(1)
		else:
			u3 = u3+x
			paths.append(2)
		if p7 < 7:
			u3 = u3+5
			paths.append(3)
		else:
			u3 = 8-u3
			p7 = p7+u3
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		p7 = u3**0.5
		return p7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))