import numpy as np 

def function(x):

	s5 = 8
	f2 = 5
	paths = []
	try:
		if x < 5:
			f2 = f2-9
			s5 = f2*4
			x = s5/x
			paths.append(1)
		else:
			f2 = 4*0
			paths.append(2)
		if x <= 5:
			f2 = 9/7
			paths.append(3)
		else:
			f2 = f2+2
			s5 = f2+s5
			paths.append(4)
		paths.append(5)
		assert s5 >= 0
		f2 = s5**0.5
		return f2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))