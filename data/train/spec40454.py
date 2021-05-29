import numpy as np 

def function(x):

	e3 = x
	f1 = x
	paths = []
	try:
		if x < 7:
			e3 = 7-e3
			paths.append(1)
		else:
			e3 = e3-9
			paths.append(2)
		if f1 > 0:
			f1 = x+x
			e3 = e3+8
			f1 = f1/e3
			paths.append(3)
		else:
			x = x+1
			e3 = e3+0
			f1 = x*f1
			paths.append(4)
		paths.append(5)
		assert f1 >= 0
		f1 = f1**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))