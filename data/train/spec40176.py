import numpy as np 

def function(x):

	w5 = 5
	r8 = 7
	paths = []
	try:
		if w5 <= 3:
			r8 = x*1
			w5 = w5+5
			r8 = x-6
			paths.append(1)
		else:
			x = 8*x
			x = w5+9
			x = w5*7
			paths.append(2)
		if r8 <= 4:
			r8 = r8+1
			w5 = x+w5
			paths.append(3)
		else:
			w5 = r8/w5
			w5 = 3-5
			paths.append(4)
		paths.append(5)
		assert w5 >= 0
		x = w5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))