import numpy as np 

def function(x):

	f2 = x
	o7 = 9
	x = x
	paths = []
	try:
		if f2 >= 6:
			x = 4/o7
			x = 7+x
			paths.append(1)
		else:
			x = 4+x
			o7 = o7*f2
			o7 = x*1
			paths.append(2)
		if f2 > 9:
			f2 = f2/5
			paths.append(3)
		else:
			o7 = 1*2
			o7 = o7-2
			x = o7-7
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