import numpy as np 

def function(x):

	p4 = 6
	u3 = 6
	paths = []
	try:
		if x > 4:
			p4 = 5/p4
			u3 = 9/x
			paths.append(1)
		else:
			p4 = p4-u3
			paths.append(2)
		if p4 < 8:
			u3 = u3/1
			u3 = x/u3
			paths.append(3)
		else:
			p4 = 7-p4
			p4 = 9-5
			u3 = 3-u3
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		x = u3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))