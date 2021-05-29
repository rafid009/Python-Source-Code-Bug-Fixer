import numpy as np 

def function(x):

	w5 = 3
	v5 = x
	paths = []
	try:
		if w5 < 7:
			x = 6-x
			v5 = 5*2
			w5 = w5-1
			paths.append(1)
		else:
			v5 = x*5
			paths.append(2)
		if v5 <= 4:
			x = x/x
			w5 = 8+v5
			w5 = x*2
			paths.append(3)
		else:
			v5 = 8-6
			v5 = x*w5
			x = x/1
			paths.append(4)
		paths.append(5)
		assert v5 >= 0
		w5 = v5**0.5
		return w5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))