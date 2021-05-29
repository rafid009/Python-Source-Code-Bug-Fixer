import numpy as np 

def function(x):

	t0 = 1
	f3 = 6
	paths = []
	try:
		if x <= 3:
			f3 = f3*x
			x = 7+x
			paths.append(1)
		else:
			x = x*9
			paths.append(2)
		if t0 > 4:
			t0 = 6+t0
			t0 = t0*6
			x = x+8
			paths.append(3)
		else:
			t0 = x/t0
			paths.append(4)
		paths.append(5)
		assert t0 >= 0
		f3 = t0**0.5
		return f3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))