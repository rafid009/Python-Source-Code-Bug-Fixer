import numpy as np 

def function(x):

	u3 = 2
	p9 = 4
	paths = []
	try:
		if p9 > 6:
			u3 = u3-0
			x = x-x
			p9 = 5/p9
			paths.append(1)
		else:
			u3 = 5*x
			paths.append(2)
		if p9 <= 9:
			p9 = x*9
			paths.append(3)
		else:
			x = x*8
			u3 = p9+p9
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		u3 = u3**0.5
		return u3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))