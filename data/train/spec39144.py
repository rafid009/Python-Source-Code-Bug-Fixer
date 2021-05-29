import numpy as np 

def function(x):

	f2 = 1
	e5 = 7
	paths = []
	try:
		if e5 <= 2:
			f2 = f2*9
			f2 = 3/1
			e5 = 6+e5
			paths.append(1)
		else:
			f2 = f2+x
			paths.append(2)
		if x > 1:
			x = 3/x
			e5 = e5+f2
			e5 = 6/6
			paths.append(3)
		else:
			e5 = x*3
			paths.append(4)
		paths.append(5)
		assert e5 >= 0
		f2 = e5**0.5
		return f2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))