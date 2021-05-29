import numpy as np 

def function(x):

	f2 = x
	v7 = 8
	paths = []
	try:
		if x < 2:
			v7 = 7-f2
			v7 = v7-f2
			v7 = 1-f2
			paths.append(1)
		else:
			f2 = f2/v7
			x = 2-5
			v7 = v7-x
			paths.append(2)
		if v7 <= 4:
			v7 = 4+v7
			f2 = f2*1
			paths.append(3)
		else:
			v7 = v7*v7
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