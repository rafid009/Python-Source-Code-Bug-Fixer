import numpy as np 

def function(x):

	f0 = x
	u2 = x
	x = 7
	paths = []
	try:
		if x > 1:
			f0 = f0+3
			u2 = u2-u2
			u2 = 1-9
			paths.append(1)
		else:
			f0 = u2/f0
			x = x-9
			x = x/8
			paths.append(2)
		if u2 <= 2:
			f0 = 5/f0
			paths.append(3)
		else:
			x = x*u2
			f0 = f0/9
			x = 0+1
			paths.append(4)
		paths.append(5)
		assert f0 >= 0
		f0 = f0**0.5
		return f0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))