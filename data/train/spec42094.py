import numpy as np 

def function(x):

	b1 = 3
	f4 = x
	paths = []
	try:
		if x <= 9:
			f4 = 2+f4
			f4 = f4*4
			paths.append(1)
		else:
			f4 = f4*0
			f4 = f4-x
			b1 = 0/b1
			paths.append(2)
		if b1 > 1:
			f4 = x*1
			b1 = 4+1
			x = x/9
			paths.append(3)
		else:
			x = 5-6
			f4 = f4*x
			f4 = b1*7
			paths.append(4)
		paths.append(5)
		assert f4 >= 0
		f4 = f4**0.5
		return f4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))