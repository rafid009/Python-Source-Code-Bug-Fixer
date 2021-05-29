import numpy as np 

def function(x):

	f2 = x
	u3 = x
	x = 5
	paths = []
	try:
		if u3 >= 1:
			f2 = f2/5
			u3 = 0+u3
			x = x+0
			paths.append(1)
		else:
			x = 8*x
			f2 = f2-4
			x = 2/5
			paths.append(2)
		if f2 > 8:
			u3 = 2*9
			x = 8+0
			paths.append(3)
		else:
			x = 6*3
			u3 = u3*6
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		f2 = u3**0.5
		return f2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))