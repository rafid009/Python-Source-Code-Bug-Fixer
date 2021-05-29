import numpy as np 

def function(x):

	w9 = x
	f2 = 9
	paths = []
	try:
		if f2 < 4:
			x = x*0
			f2 = f2-7
			paths.append(1)
		else:
			f2 = 6*w9
			f2 = 5+9
			paths.append(2)
		if f2 > 6:
			x = 6+x
			w9 = 3/w9
			w9 = x/4
			paths.append(3)
		else:
			w9 = 5+x
			f2 = f2+4
			paths.append(4)
		paths.append(5)
		assert w9 >= 0
		w9 = w9**0.5
		return w9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))