import numpy as np 

def function(x):

	f2 = 7
	w4 = 4
	paths = []
	try:
		if f2 >= 3:
			f2 = 3+3
			x = x-f2
			f2 = f2+f2
			paths.append(1)
		else:
			x = x*1
			x = x/x
			f2 = f2+7
			paths.append(2)
		if x < 9:
			w4 = x*9
			w4 = w4+5
			w4 = 3+9
			paths.append(3)
		else:
			x = 5+x
			w4 = w4*0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f2 = x**0.5
		return f2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))