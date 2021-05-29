import numpy as np 

def function(x):

	e4 = x
	f4 = x
	paths = []
	try:
		if e4 > 1:
			x = x*1
			paths.append(1)
		else:
			x = 8*x
			f4 = 0+f4
			f4 = 7*f4
			paths.append(2)
		if f4 <= 7:
			x = 5+8
			f4 = 0/f4
			paths.append(3)
		else:
			x = x*0
			x = e4/5
			x = f4-7
			paths.append(4)
		paths.append(5)
		assert e4 >= 0
		f4 = e4**0.5
		return f4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))