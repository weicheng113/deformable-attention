import torch
from hamcrest import assert_that

from deformable_attention import DeformableAttention1D


class TestDeformableAttention1D:
    def test_shape(self):
        attn = DeformableAttention1D(
            dim=128,
            downsample_factor=4,
            offset_scale=2,
            offset_kernel_size=6
        )

        x = torch.randn(1, 128, 512)
        out = attn(x)
        assert_that(out.shape, (1, 128, 512))
