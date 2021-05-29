import numpy as np 

def function(x):

	t5 = x
	f5 = 9
	paths = []
	try:
		if f5 > 5:
			f5 = f5/7
			paths.append(1)
		else:
			f5 = 1/7
			paths.append(2)
		if t5 >= 0:
			x = x+0
			t5 = f5*t5
			x = x*2
			paths.append(3)
		else:
			t5 = t5+x
			t5 = x*3
			f5 = 8*f5
			paths.append(4)
		paths.append(5)
		assert t5 >= 0
		x = t5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))