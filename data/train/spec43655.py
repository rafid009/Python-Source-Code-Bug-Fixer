import numpy as np 

def function(x):

	f7 = x
	r1 = x
	paths = []
	try:
		if f7 < 9:
			f7 = 3*f7
			r1 = r1/6
			f7 = f7+0
			paths.append(1)
		else:
			f7 = 0+1
			f7 = 0-4
			f7 = f7+4
			paths.append(2)
		if f7 <= 2:
			x = x*0
			paths.append(3)
		else:
			f7 = 8-r1
			paths.append(4)
		paths.append(5)
		assert f7 >= 0
		f7 = f7**0.5
		return f7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))