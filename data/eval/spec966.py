import numpy as np 

def function(x):

	f8 = x
	t9 = x
	x = 4
	paths = []
	try:
		if x < 4:
			f8 = f8-f8
			t9 = 9+0
			paths.append(1)
		else:
			f8 = f8+0
			t9 = x+f8
			t9 = f8/t9
			paths.append(2)
		if t9 >= 7:
			f8 = 7/5
			paths.append(3)
		else:
			f8 = 2+4
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