import numpy as np 

def function(x):

	f8 = 2
	t9 = x
	paths = []
	try:
		if f8 >= 2:
			x = x*1
			x = 4*x
			f8 = f8/9
			paths.append(1)
		else:
			x = x*0
			x = f8/4
			paths.append(2)
		if f8 < 7:
			f8 = 2/x
			paths.append(3)
		else:
			t9 = t9*f8
			t9 = 8+t9
			paths.append(4)
		paths.append(5)
		assert t9 >= 0
		f8 = t9**0.5
		return f8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))