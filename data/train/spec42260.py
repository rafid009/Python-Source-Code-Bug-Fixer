import numpy as np 

def function(x):

	f7 = 5
	t2 = 8
	paths = []
	try:
		if x < 4:
			t2 = 7*t2
			paths.append(1)
		else:
			x = 4*2
			x = 3*t2
			f7 = f7/f7
			paths.append(2)
		if x < 7:
			f7 = f7-5
			paths.append(3)
		else:
			f7 = f7*0
			f7 = t2-f7
			t2 = 3+t2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f7 = x**0.5
		return f7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))