# Installation

## Software
*  Python3.x (installation via [Anaconda](https://www.anaconda.com/distribution/) is recommended; **mandatory for Windows users**)
   * (Optional) It is recommended to use conda environments. Run `conda create -n vtuber python=3.6`. Activate it by `conda activate vtuber`.
*  Python libraries
   * Install Dlib 
      * `pip install https://pypi.python.org/packages/da/06/bd3e241c4eb0a662914b3b4875fc52dd176a9db0d4a2c915ac2ad8800e9e/dlib-19.7.0-cp36-cp36m-win_amd64.whl#md5=b7330a5b2d46420343fbed5df69e6a3f`
   * Ubuntu:
      * Install the requirements by `pip install -r requirements_(cpu or gpu).txt`
      * If you have CUDA 10.1, `pip install onnxruntime-gpu` to get faster inference speed using onnx model.
   * Windows:
      * CPU:
         *  `pip install -r requirements_cpu.txt`
         *  if [dlib](https://github.com/davisking/dlib) cannot be properly installed, follow [here](https://github.com/kwea123/VTuber_Unity/wiki/Dlib-installation-on-Windows).
      * GPU: 
         * Install [pytorch](https://pytorch.org/) using `conda`. Example: `conda install pytorch==1.2.0 torchvision==0.4.0 cudatoolkit=10.0 -c pytorch`
         * Install other dependencies by `pip install -r requirements_gpu.txt`.
         * If you have CUDA 10, `pip install onnxruntime-gpu` to get faster inference speed using onnx model.
           
*  Optional
   *  Unity Editor if you want to customize the virtual character.
        *  [Linux installation](https://forum.unity.com/threads/unity-on-linux-release-notes-and-known-issues.350256/)
        *  [Windows installation](https://unity3d.com/get-unity/download)

## 0.  Model download
You need to download the models [here](https://github.com/kwea123/VTuber_Unity/releases/tag/v1.0), extract and put into `face_alignment/ckpts`.

If you don't use `onnxruntime`, you can omit this step as the script will automatically download them for you.

## 1.  Face detection test
Run `python demo.py --debug`. (add `--cpu` if you have CPU only)

## 2.  Synchronize with the virtual character
1.  Download and launch the binaries [here](https://github.com/kwea123/VTuber_Unity/releases) depending on your OS to launch the unity window featuring the virtual character (unity-chan here).
**Important: Ensure that only one window is opened at a time!**
2.  After the vitual character shows up, run `python demo.py --connect` to synchronize your face features with the virtual character. (add `--debug` to see your face and `--cpu` if you have CPU only as step 1.)
