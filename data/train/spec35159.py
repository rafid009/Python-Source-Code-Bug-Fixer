import numpy as np 

def function(x):

	r8 = x
	m9 = 1
	paths = []
	try:
		if x > 9:
			x = x+x
			paths.append(1)
		else:
			m9 = m9-4
			paths.append(2)
		if m9 < 1:
			x = x*0
			r8 = m9-6
			paths.append(3)
		else:
			x = m9*x
			x = x/m9
			m9 = m9-6
			paths.append(4)
		paths.append(5)
		assert r8 >= 0
		r8 = r8**0.5
		return r8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))