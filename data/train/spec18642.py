import numpy as np 

def function(x):

	b4 = 6
	f1 = x
	paths = []
	try:
		if f1 > 8:
			b4 = b4*2
			paths.append(1)
		else:
			b4 = b4-6
			paths.append(2)
		if f1 <= 0:
			x = x+5
			x = x/x
			b4 = 5+b4
			paths.append(3)
		else:
			b4 = b4+f1
			b4 = b4*4
			b4 = 6/1
			paths.append(4)
		paths.append(5)
		assert f1 >= 0
		f1 = f1**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))