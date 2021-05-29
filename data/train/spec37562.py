import numpy as np 

def function(x):

	f3 = x
	u3 = x
	x = x
	paths = []
	try:
		if f3 < 4:
			u3 = 2-u3
			paths.append(1)
		else:
			u3 = 0/u3
			f3 = f3/4
			paths.append(2)
		if f3 < 4:
			f3 = f3+x
			paths.append(3)
		else:
			x = x*f3
			paths.append(4)
		paths.append(5)
		assert f3 >= 0
		f3 = f3**0.5
		return f3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))