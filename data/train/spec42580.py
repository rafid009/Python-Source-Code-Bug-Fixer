import numpy as np 

def function(x):

	a2 = 9
	u3 = 2
	x = x
	paths = []
	try:
		if x <= 6:
			u3 = x*8
			a2 = a2/u3
			a2 = 1+a2
			paths.append(1)
		else:
			x = x+x
			paths.append(2)
		if u3 > 6:
			x = a2-a2
			u3 = 8+u3
			a2 = x+2
			paths.append(3)
		else:
			u3 = 9/a2
			u3 = u3+a2
			u3 = 2-u3
			paths.append(4)
		paths.append(5)
		assert a2 >= 0
		a2 = a2**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))