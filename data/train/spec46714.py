import numpy as np 

def function(x):

	e7 = x
	f2 = x
	paths = []
	try:
		if f2 < 2:
			e7 = e7*e7
			x = e7*8
			paths.append(1)
		else:
			f2 = 4+f2
			f2 = 5-1
			paths.append(2)
		if e7 > 8:
			x = e7-e7
			f2 = f2-7
			paths.append(3)
		else:
			e7 = e7+3
			paths.append(4)
		paths.append(5)
		assert f2 >= 0
		f2 = f2**0.5
		return f2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))