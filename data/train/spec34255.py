import numpy as np 

def function(x):

	r2 = x
	f3 = x
	paths = []
	try:
		if r2 <= 6:
			r2 = r2*7
			x = 3+9
			paths.append(1)
		else:
			r2 = r2/5
			r2 = r2-3
			r2 = 3-r2
			paths.append(2)
		if f3 >= 7:
			f3 = f3-x
			paths.append(3)
		else:
			f3 = 5+f3
			f3 = 5*f3
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