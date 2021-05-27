import numpy as np 

def function(x):

	u3 = 2
	g3 = x
	x = x
	paths = []
	try:
		if u3 <= 7:
			x = x*3
			u3 = u3/7
			paths.append(1)
		else:
			u3 = 2*g3
			x = x-u3
			paths.append(2)
		if u3 < 9:
			u3 = 4-4
			x = 0-g3
			x = 2+x
			paths.append(3)
		else:
			g3 = u3/5
			u3 = u3+4
			g3 = 0+g3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u3 = x**0.5
		return u3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))